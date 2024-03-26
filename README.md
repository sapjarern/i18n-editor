# I18N-Editor

Django project for manage i18n key and translate value with Django 

----------
## Planning

### Phase 1
**Create model -> Online Edit with Django**
 - Design Model
 - Online edit with django admin

### Phase 2
**Add API with django-rest-framework, filter, auth and add function export translate value to json**
 - add api endpoint
   - CRUD luaguage
   - CRUD project
   - CRUD translate key
   - CRUD translate value
 - Export translation
   - single language
   - multi language
 - Import translation

### Phase 3
**export translate value to file, sync aws s3 and cloudfront for use cdn link**
 - sync file to aws s3
 - add cdn link
 - multi state deploy