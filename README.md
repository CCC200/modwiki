# modwiki
Create self-updating dex sites for Pokemon Showdown mods.

[!IMPORTANT]
This repo is primarily setup to support a single mod that is being maintained by the repo owner. It might support others out of the box, but expect the possibility of needing to change the codebase.

## Setup
1. Fork the repo and clone it to a machine capable of serving to your webserver/pages site etc.
2. Open `py/cache.py` and set the `repo` value to your pokemon-showdown server repository, and `mod` to the name of the mod folder the wiki will pull data from.
3. Open `py/pager.py` and set `site_title` to something appropriate for the mod.

## Building
Creating the site is simple: run `build.py` from the root of the repo, and the new `_site` directory will contain all the page files. Point your webserver there, or copy it etc. There are no other dependencies or requirements, since the site is pure HTML/JS/CSS.
