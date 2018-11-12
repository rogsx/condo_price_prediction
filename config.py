class Config:
    RAW_COL_NAMES = ['id', 'link', 'name', 'size_range', 'listing_price',
                     'price_per_ft2', 'bed', 'shower', 'parking', 'dom',
                     'maint_fee', 'region', 'street', 'unit_num', 'latitude',
                     'longitude', 'locker', 'taxes', 'exposure', 'balcony',
                     'description', 'pics', 'floorplans']

    ENCODING_CONFIG = {
        'CAT_COLS': ['balcony', 'bed', 'exposure', 'locker'],
        'BINARY_COLS': ['parking']
    }
