# Fleamarkt - marketplace bot for discord community

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from objects import Product, Inventory

load_dotenv()
FLEAMARKT_TOKEN = os.getenv('FLEAMARKT_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='sell')
async def sell(ctx, what: str, category: str, price: float):

    # add a new product for sale
    inventory.add_product(Product(what, price, ctx.author.id, category))
    await ctx.send(f'You have successfully added a new product for sale!')

    # announce it in the marketplace channel
    marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
    await marketplace_channel.send(f'{ctx.author.mention} added {what.title()} for sale. Check it out!')
    embed = discord.Embed(title=f'{what.title()}',
                          description=f'category: {category}, price: {price}',
                          color=discord.Colour.green())
    await marketplace_channel.send(embed=embed)


@bot.command(name='buy')
async def buy(ctx, buy_id: int):

    # check for product by ID
    for product in inventory.for_sale:
        if product.id == buy_id:
            # get owner of the product
            owner = await bot.fetch_user(product.owner)

            # prepare message
            embed = discord.Embed(title=f'{product.name.title()}',
                                  description=f'category: {product.category}, price: {product.price}',
                                  color=discord.Colour.red())
            # inform buyer
            await ctx.send(f'You have successfully bought {product.name.title()}')
            await ctx.send(embed=embed)
            await ctx.send(f'Now contact {owner.mention} for payment!')

            # inform owner
            await owner.send(f'Your {product.name.title()} was just!')
            await ctx.send(embed=embed)
            await owner.send(f'Prepare item for sale and contact {ctx.author.mention} for payment!')

            # inform market
            marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
            await marketplace_channel.send(
                f'$$$ {ctx.author.mention} have just bought {product.name.title()} from {owner.mention} $$$')
            await marketplace_channel.send(embed=embed)

            # delete product from the list for sale
            inventory.del_product(product.id)
            break
    else:
        # no such product on the list
        await ctx.send('I cannot find such a product for sale :(')
        await ctx.send('To buy a product provide an ID of the product that you are interested in.')
        await ctx.send('To see list of available products with their IDs use *!show* command.')


@bot.command(name='show')
async def show(ctx, n: str = '5'):

    # for 'all' flag list all products, else take n last products
    if n == 'all':
        n = int(len(inventory.for_sale))
    else:
        n = int(n)

    # show list of products
    embed = discord.Embed(title=f'Items for sale:',
                          description=f'You asked for {n} last added products.',
                          color=discord.Colour.blue())

    if not inventory.for_sale:
        embed.add_field(name=f'No products.', value='I have nothing for sale :(')
    else:
        for product in inventory.last_n_products(n):
            embed.add_field(name=f'{product.name.title()}',
                            value=f'ID: {product.id}, category: {product.category}, price: {product.price}',
                            inline=False)
    await ctx.send(embed=embed)


@bot.command(name='want')
async def want(ctx, thing: str, cost: float):

    # inform marketplace channel
    marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
    await marketplace_channel.send(
        f"{ctx.author.mention} is looking for {thing.title()}. \
        Check your stuff, maybe you don't need it and you can sell it.")

    # prepare message
    embed = discord.Embed(title=f'{thing.title()}',
                          description=f'cost around: {cost}',
                          color=discord.Colour.dark_gold())
    await marketplace_channel.send(embed=embed)


@bot.command(name='delete')
async def delete(ctx, id: int):
    # check if such a product exists
    for product in inventory.for_sale:
        if product.id == id:
            if product.owner == ctx.author.id:
                # prepare message
                embed = discord.Embed(title=f'{product.name.title()}',
                                      description=f'category: {product.category}, price: {product.price}',
                                      color=discord.Colour.red())
                # inform user
                await ctx.send('You have successfully removed your product from the marketplace.')
                await ctx.send(embed=embed)

                # inform marketplace
                marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
                await marketplace_channel.send(
                    f"Item {product.name.title()} was removed from the marketplace by its owner.")
                await marketplace_channel.send(embed=embed)
                await marketplace_channel.send(f"It's no longer for sale.")
                inventory.del_product(product.id)
                break
            else:
                # don't allow to delete product of different user
                await ctx.send('Product exists but you are not the owner of the product so you cannot delete it.')
                break
    else:
        # no such product on the list
        await ctx.send('I cannot find such a product for sale :(')
        await ctx.send('To remove a product provide an ID of the product that you want to remove.')
        await ctx.send('To see list of available products with their IDs use *!show* command.')

# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)  # without this the whole script is dying
#     print(message)

# init inventory for the bot
inventory = Inventory()

bot.run(FLEAMARKT_TOKEN)
