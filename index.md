## Welcome to the docs for Isiaiah

The main hub for documentation regarding Isiaiah.

### Examples

All examples are within the style guidelines of codestyle black.

__**Isaiah Class Usage**__
```py
from core import Isaiah
from core import Context

bot = Isaiah()

```

__**Context Class Usage**__
```py
@bot.command()
async def hi(ctx: Context):
    """Returns hello.
    
    Parameters:
      ctx: core.Context - The command context.
    """
    if ctx.message.content != "hi":
      return ctx.error("Error: Does not compute")
    
    return ctx.send("Hello!")
```

__**Basic Usage**__
```py
from core import Isaiah
from core import Context

bot = Isaiah()

@bot.command()
async def hi(ctx: Context):
    """Returns hello.
    
    Parameters:
      ctx: core.Context - The command context.
    """
    if ctx.message.content != "hi":
      return ctx.error("Error: Does not compute")
    
    return ctx.send("Hello!")
```

