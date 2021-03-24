#!/usr/bin/env python3
#
#

import sys
import http
import uuid
import json
import time

import flask


# Standard flask setup:
app = flask.Flask(__name__)

# Used for cookie domains
CRICUT_COM = '.cricut.com'


# DESIGN NOTES
#
# The handlers generally use request.args['NAME'] to fetch the expected
# argument values. If that throws a KeyError, then Flask turns that into
# a 400 response. This should be fine for an API rather than a website
# presented directly to users.
#


#------------------------

@app.route('/content/Fonts/ByName')  # ?familyName=Cricut%20Sans
def fonts_byname():
    family = flask.request.args['familyName']

@app.route('/content/Fonts/Get')  # ?fontId=1234
def fonts_get():
    font_id = flask.request.args['fontId']

@app.route('/content/Fonts/GetAllCharsForFontV2')  # ?fontId=1234
def fonts_get_allchars():
    font_id = flask.request.args['fontId']

#------------------------

@app.route('/content/ImageCategories/ImageCategoriesForImage')  # imageId=1234567
def image_cats():
    image_id = flask.request.args['imageId']

@app.route('/content/ImageSet/GetImageSet')  # ImageSetID=123456
def image_set():
    set_id = flask.request.args['ImageSetID']

@app.route('/content/Images/Get')  # Id=1234567
def image_get():
    image_id = flask.request.args['Id']

@app.route('/content/Images/PushUserImagesToSearch')
def image_push():
    pass

@app.route('/content/Images/v3/GetCanvasImage')  # inImageIDs=...
def image_canvas():
    ids = flask.request.args['inImageIDs']
    images = ids.split(',')  # 1 or more

#------------------------

@app.route('/images/FontFamilies')  # size=1234
def font_families():
    size = flask.request.args['size']

@app.route('/images/v1/images/categories/headers')
def categ_headers():
    pass

@app.route('/images/v1/images/filterTypes')  # ?machineFamilyType=MAKE_FAMILY
def image_filters():
    # The machineFamily request arg appears to be optional
    family = flask.request.get('machineFamilyType')  ### default?

#------------------------

@app.route('/materialsMachineFamilies')  # machineTypeIdsToInclude
def machine_families():
    ids = flask.request.args['inImageIDs']
    types = [t.strip() for t in ids.split(',') ]
    sortby = flask.request.get('sortBy')  # optional  ### default?

@app.route('/materials/Machines/registered')
def machines_registered():
    pass

#------------------------

@app.route('/pens/Pens')  # ?version=2
def pens():
    vsn = flask.request.args['version']

#------------------------

@app.route('/profiles/v1/Profiles/<user_id>/social')
def profiles_social(user_id):
    pass

@app.route('/profiles/v1/Profiles/<user_id>/follows/profiles/<user_follow>')
def profiles_follows(user_id, follow):
    pass

@app.route('/profiles/v1/Profiles/cricutId/<id>')
def profiles_cricut(id):
    pass

#------------------------

@app.route('/projects/CanvasMigrationQueue')
def projects_migration():
    pass

@app.route('/projects/Projects/v1/userProjects/<user_id>')
def projects_fetch(user_id):
    token = flask.request.args.get('token')
    size = flask.request.args.get('size')
    pub_only = flask.request.args.get('publishedOnly')

@app.route('/projects/v1/Projects/search')
def projects_search():
    entitled = flask.request.args.get('entitledOnly')
    level = flask.request.args.get('projectDetailLevel')
    featured = flask.request.args.get('featured')
    size = flask.request.args.get('size')
    token = flask.request.args.get('token')
    family = flask.request.args.get('machineFamilyType')
    type = flask.request.args.get('type')
    translate = flask.request.args.get('translateQuery')

@app.route('/projects/v1/projects/favorites/<user_id>')  # ?size=200
def projects_favs(user_id):
    size = flask.request.args['size']

#------------------------

@app.route('/tags/v1/Categories')
def tags():
    is_community = flask.request.args.get('isCommunity')
    family = flask.request.args.get('machineFamilyType')
    size = flask.request.args.get('pageSize')
    type = flask.request.args.get('type')
    include_subcat = flask.request.args.get('includeSubCategories')

#------------------------

@app.route('/v4/Entitlements/GetImageSetGroupExpirations')
def v4_expirations():
    pass

@app.route('/v4/Lookups/GetAppSessionData')  # appName=Gliese
def v4_get_session():
    app = flask.request.args['appName']
    sid = uuid.uuid4()

    ### no idea what each element represents, but this is the order
    ### and the values that upstream delivers
    body = (
        'https://imgservice.cricut.com/design-public-mirror1/images/',
        'https://imgservice.cricut.com/design-public-mirror1/templates/',
        '-api.cricut.com/v4/Images/GetUserImage?ImageID=',
        '',
        '',
        '100',
        '151',
        '',
        '1-1-1',
        'http://mirror.cricut.com/project/',
        '1',
        '51766',
        KEPLER_J,
        'https://imgservice.cricut.com/design-public-mirror1/software/',
        'https://imgservice.cricut.com/design-public-mirror1/categories/',
        'V4',
        'https://s3-us-west-2.amazonaws.com/dev50-design-public/Fonts/',
        str(int(time.time())),
        )
    ### maybe ensure the C-T includes the charset?
    response = flask.make_response(flask.jsonify(body))
    response.set_cookie('SessionID-Prod', str(sid),
                        expires=None,  ### fix this
                        path='/',
                        domain=CRICUT_COM,
                        )
    ### fix these country values
    ### US=312, BE=334
    response.set_cookie('SelectedCountryID', '312',
                        domain=CRICUT_COM, path='/')
    response.set_cookie('Country-Code', 'US',
                        domain=CRICUT_COM, path='/')
    ### other response headers?
    return response

KEPLER = {
    "Kepler": {
        "Windows": {
            "Available": {
                "Version": "3.2.1.0",
                "File": "CricutDesignSpace-3.2.1.0.exe",
                "Type":"Optional",
            },
            "Required": {
                "Version": "3.2.1.0",
                "File": "CricutDesignSpace-3.2.1.0.exe",
                "Type": "Required",
            },
        },
        "MacOS": {
            "Available": {
                "Version": "3.2.1.0",
                "File": "CricutDesignSpace-3.2.1.0.zip",
                "Type": "Optional",
            },
            "Required": {
                "Version": "3.2.1.0",
                "File": "CricutDesignSpace-3.2.1.0.zip",
                "Type": "Required",
            },
            },
        },
    }
KEPLER_J = json.dumps(KEPLER)

@app.route('/v4/ShoppingCart/Quote')
def v4_shopping_quote():
    pass

@app.route('/v4/Subscription/PurchasableSubscriptions')
def v4_purchasable():
    pass

@app.route('/v4/Subscription/UserCricutAccessStatus')
def v4_user_status():
    pass

@app.route('/v4/Users/GetLoggedInUser')
def v4_get_user():
    pass

@app.route('/v4/Users/GetUserPreferencesAsync')
def v4_get_prefs():
    pass

@app.route('/v4/Users/IsUserLoggedIn')
def v4_is_loggedin():
    pass

@app.route('/v4/Users/Login')
def v4_login():
    pass

@app.route('/v4/Users/SaveUserPreferencesAsync')
def v4_save_prefs():
    pass

#------------------------


if __name__ == '__main__':
    # Run the daemon, listening at paths noted above.
    app.run(debug=True, host='0.0.0.0')
