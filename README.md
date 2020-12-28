# Python Migration System

This is a pack of scripts to Run a simple migration system in MongoDB Databases out of the box.

[![Build Status](https://travis-ci.com/plazari15/python-migrator.svg?branch=main)](https://travis-ci.com/plazari15/python-migrator)


# How To Setup In My Project?
================================================================================
1. clone this repository to the root of your project.
2. if you want, you can copy `migrator` to the root of your project, but dont forget to make the correct adjusts in the file
    a. if you decide to change migrator file of place You'll need to change lines 10,11 
        `MIGRATIONS_FOLDER` and `DOCKER_FILE`
3. You Can change the migrations folder too, if your project have your own migrations folder, you can point to same place.
4. if your project have your own envs you can change it in the file config/mongodb.py
5. Define Network in docker run command add this before image name `--network bubble /\`
# How To Run?
================================================================================
1. Dont Forget the folder where you put you `migrator`

### Generate Migration File
`./migrator generate name_of_your_migration`

if you'd like to force another image build

`./migrator generate name_of_your_migration --build`

### Run Migration
`./migrator migrate`

if you'd like to force another image build

`./migrator migrate --build`

### Run Rollback of Migrations
`./migrator rollback`

if you'd like to force another image build

`./migrator rollback --build`

## If I forget the commands?
`./migrator --help`

# TODO
================================================================================
- Improve Code
- Create UnitTests (using pytest)
- Install TravisCI to run tests automatically
- Create Integrations with other databases

Contributing
================================================================================

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

