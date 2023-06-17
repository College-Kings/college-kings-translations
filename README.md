# College Kings Translation Files

## Tutorials

### How to start translating a new part:
1. Fork the repository.
2. Clone the GitHub repository to your PC.
3. Find your language folder. If your language doesn't exist copy the `copy-me` folder and rename it accordingly.
4. Open a file and start translating:
```
# game/script.rpy:95
translate piglatin start_636ae3f5:

    # e "Thank you for taking a look at the Ren'Py translation framework."
    e "Thank you for taking a look at the Ren'Py translation framework."
```
The line starting with `#` is the English sentence
The line starting with `e` is what you need to replace with the translated sentence

```
```
translate piglatin strings:

    old "Eileen"
    new "Eileen"
  ```
The line starting with `old` is the English sentence
The line starting with `new` is what you need to replace with the translated sentence


### How to add a newly translated part:
1. Make sure your commits and edits are pushed to your forked repository.
2. Create a Pull Request to be reviewed and merged.

Have fun!
