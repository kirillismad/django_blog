from drf_yasg.openapi import Schema

sign_in = {
    '200': Schema(type='object',
                  properties={'token': Schema(type='string', title='JWToken'),
                              'id': Schema(type='integer', title='user ID')},
                  required=['id', 'token'])
}
