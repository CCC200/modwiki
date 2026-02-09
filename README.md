# modwiki
#### [Demo Site](https://polishedwiki.github.io/])
Create self-updating dex sites for Pokemon Showdown mods.

> [!IMPORTANT]
> This repo is primarily designed to support my own mod. It might support others out of the box but expect the possibility of needing to change the codebase.

## Setup
Select **Use this template > Create a new repository** to fork the repo. Clone it to your machine, then edit the following files to be suitable for your mod: 
1. Open `py/cache.py` and set the `repo` value to your pokemon-showdown server repository, and `mod` to the name of the mod folder the wiki will pull data from.
2. Open `py/pager.py` and set `site_title` to something appropriate for the mod.
3. You may also want to change `pages/assets/favicon.ico` to a custom icon.

## Github Pages
If you'd wish to have your wiki automatically hosted on pages, there is a workflow already setup:
1. Follow the steps above to create your repo, matching the standard `[name].github.io` format for the repo name.
2. Go to **Settings > Pages** and set **Branch** to `gh-pages`

That's it! Your site will automatically rebuild on new commits. If you need to manually force a rebuild (for example, if you update your showdown mod without any changes on this repo) go to **Actions > Build and Deploy** and select **Run workflow**.

## Building (local)
Creating the site is simple: run `build.py` from the root of the repo, and the new `_site` directory will contain all the page files. Point your webserver there, or copy it etc. There are no other dependencies or requirements, since the site is pure HTML/JS/CSS.
