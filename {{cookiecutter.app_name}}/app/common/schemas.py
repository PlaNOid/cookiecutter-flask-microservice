from webargs import fields

FILTER_SCHEMA = {
    'page': fields.Int(missing=1),
    'limit': fields.Int(missing=10),
    'sort_by': fields.Str(missing='-created_at')
}
