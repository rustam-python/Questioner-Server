from flask_restplus import Api

api = Api(title='REST API',
          version='1.0',
          description='A description',
          default='Title',
          default_label='Subtitle',
          doc='/api', prefix='/api')
