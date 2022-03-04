# Django Models

+ *In this app we build out a small, but functional, multi page web site that utilizes a database and authorized users to present information using Django Models.*

## Feature Tasks and Requirements

+ Model
  + create snack_tracker_project project
  + create snacks app
  + Add snacks app to project
  + create Snack model
    + extends from proper base class
    + add name as a CharField with maximum length of 64 characters.
    + add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    + add description TextField
  + add model to admin
  + modify Snack model have user friendly display in admin
+ create migrations and migrate data
+ create a super user
+ Add a few snacks via Admin panel
+ create another user and more snacks via Admin panel

+ Views for Snacks App
  + create SnackListView
  + give a template of snack_list.html
  + associate Snack model
+ update url patterns for project
  + empty path should include snacks.urls
  + update snacks app urls
  + empty sub-path should be handled by SnackListView
  + Don’t forget to use as_view()
+ add detail view
+ link snack_detail.html template
+ associate Snack model
+ update app urlpatterns to handle detail view
+ account for primary key in url

+ Templates
  + Add templates folder in root of project
  + register templates folder in project settings TEMPLATES section
  + create base.html ancestor template
  + add main html document
  + use Django Templating Language to allow child templates to insert content
  + create snack_list.html template
  + extend base template
  + create snack_detail.html template
  + template should extend base
+ content should display snack’s name, description and purchaser
+ add link in snack_list template to related detail page for each snack
+ Add a link back to Home (aka snack_list) page from detail page.

### Deployed URLs

+ **Running Server:** localhost

### Pull Request

+ [snack-tracker-project/pull/1](URL 'https://github.com/micgreene/snack-tracker-project/pull/1')

### README

+ [README.md](URL 'https://github.com/micgreene/snack-tracker-project/blob/master/README.md')
