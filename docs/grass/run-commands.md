# Run Commands

## Commands

All arguments except the first are keyword arguments, i.e. `arg=val`.
For flags, use `flags='g'`.

| Command | Description |
|---------|-------------|
| `grass.parse_command()` | Calls read commands, useful for obtaining information from `g.region`, `g.proj`, `r.info`, etc. |
| `grass.run_command()` | Calls a command and does not return until the command has finished. |

With this GRASS command:

```
r.profile -g input=mymap@PERMANENT output=newfile profile=12244.256,-295112.597,12128.012,-295293.77
```

This is how to run it with Python:

```python
>>> grass.run_command('r.profile', flags='g', input='mymap@PERMANENT', output='newfile', profile=[12244.256,-295112.597,12128.012,-295293.77])
```

Multiple flags (e.g., `-z` and `-q`) are combined as:

```python
>>> grass.run_command('r.buffer', flags='zq', input='elevation@PERMANENT', output='elev_buff')
```
