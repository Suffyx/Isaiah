## Welcome to the docs for Isiaiah

The main hub for documentation regarding Isiaiah.

### Examples

All examples are within the style guidelines of codestyle black.

__Isaiah Class Usage__
```py
from core import Isaiah
from core import Context

bot = Isaiah()

```

__Context Class Usage__
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

__Basic Usage__
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

Copyright (c) 2021-Present Suffyx
