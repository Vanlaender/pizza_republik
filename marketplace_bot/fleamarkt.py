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


@bot.command(name='sell', help="Puts your item in the marketplace for sale. After command 3 arguments must be "
                               "provided -> !sell <what> <category> <price>")
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


@bot.command(name='buy', help="Buys an item from the marketplace. After command an ID of the item must be provided -> "
                              "!buy <item_id>")
async def buy(ctx, item_id: int):

    # check for product by ID
    for product in inventory.for_sale:
        if product.id == item_id:
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


@bot.command(name='show', help="Shows n recently added product to the marketplace. After command specific number must "
                               "be provided or 'all'")
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


@bot.command(name='want', help="Informs all users in the marketplace channel, that you are looking for something "
                               "specific. After command 2 arguments must be provided -> !want <what> <cost>")
async def want(ctx, what: str, cost: float):

    # inform marketplace channel
    marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
    await marketplace_channel.send(
        f"{ctx.author.mention} is looking for {what.title()}. \
        Check your stuff, maybe you don't need it and you can sell it.")

    # prepare message
    embed = discord.Embed(title=f'{what.title()}',
                          description=f'cost around: {cost}',
                          color=discord.Colour.dark_gold())
    await marketplace_channel.send(embed=embed)


@bot.command(name='delete', help="You can delete your product from the marketplace. After command an ID of the item "
                                 "must be provided -> !delete <item_id>")
async def delete(ctx, item_id: int):
    # check if such a product exists
    for product in inventory.for_sale:
        if product.id == item_id:
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


@bot.event
async def on_message(message):
    # check if a message was sent on marketplace channel
    if message.channel.id == 916034270999507034:
        # if it was not a bot then delete the message and dm the author of the message
        if message.author.id != 915224166825877556:
            marketplace_channel = bot.get_channel(916034270999507034)  # marketplace channel id
            await marketplace_channel.purge(limit=1)
            await message.author.send(f"Hey you! It's me, Fleamarkt bot.\n" \
                                      f"I would like to remind you that I'm the only one allowed to " \
                                      f"text in the 'marketplace' channel.\n" \
                                      f"If you want to make use of marketplace, communicate with me here.\n" \
                                      f"Don't be shy to type *!help* if you don't know how I work :)\n")
    else:
        await bot.process_commands(message)

# init inventory for the bot
inventory = Inventory()

bot.run(FLEAMARKT_TOKEN)
