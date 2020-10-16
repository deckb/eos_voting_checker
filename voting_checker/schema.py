import colander

class StringReqSchema(colander.SchemaNode):
    schema_type = colander.String
    required = True

class StringOptSchema(colander.SchemaNode):
    schema_type = colander.String
    required = False
    missing = ""
    default = ""

class GithubUserSchema(colander.SchemaType):
    required = False
    missing = ""
    default = ""

    def serialize(self, node, appstruct):
        if appstruct is colander.null:
            return colander.null
        impl = colander.SequenceSchema
        if isinstance(appstruct, str):
            impl = StringOptSchema()
        return impl.serialize(node, appstruct)
    
    def deserialize(self, node, cstruct):
        return cstruct

class DecimalSchema(colander.SchemaNode):
    schema_type = colander.Decimal
    required = True

class LocationSchema(colander.MappingSchema):
    required = True
    name = StringReqSchema()
    country = StringReqSchema()
    latitude = DecimalSchema()
    longitude = DecimalSchema()

class BrandingSchema(colander.MappingSchema):
    required = False
    logo_256 = StringReqSchema()
    logo_1024 = StringReqSchema()
    logo_svg = StringReqSchema()

class SocialSchema(colander.MappingSchema):
    required = False
    facebook = StringOptSchema()
    github = StringOptSchema()
    keybase = StringOptSchema()
    reddit = StringOptSchema()
    steemit = StringOptSchema()
    telegram = StringOptSchema()
    twitter = StringOptSchema()
    wechat = StringOptSchema()
    youtube = StringOptSchema()

class NodeSchema(colander.MappingSchema):
    required = True
    location = LocationSchema()
    node_type = StringReqSchema()
    p2p_endpoint = StringOptSchema()
    api_endpoint = StringOptSchema()
    ssl_endpoint = StringOptSchema()

class NodesSchema(colander.SequenceSchema):
    nodes = NodeSchema()

class OrgSchema(colander.MappingSchema):
    candidate_name = StringReqSchema()
    website = StringReqSchema()
    code_of_conduct = StringOptSchema()
    email = StringOptSchema()
    location = LocationSchema()
    branding = BrandingSchema()
    social = SocialSchema()
    github_user = GithubUserSchema()

class BpJsonSchema(colander.MappingSchema):
    producer_account_name = StringReqSchema()
    producer_public_key = StringOptSchema()
    org = OrgSchema()
    nodes = NodesSchema()