# -*- coding: utf-8 -*-


def format_price(currency_symbol, min_price, max_price, unit, interval, hours_for_price=None):
    """Format a price string"""
    if hours_for_price:
        return u'{} for {}{}'.format(hours_for_price, currency_symbol, min_price)

    if min_price is None:
        raise TypeError('min_price should be string or integer, not None')
    formatted_price = u'{}{}'.format(currency_symbol, min_price)
    if max_price:
        formatted_price += u' to {}{}'.format(currency_symbol, max_price)
    if unit:
        formatted_price += ' per ' + unit.lower()
    if interval:
        formatted_price += ' per ' + interval.lower()
    return formatted_price


def format_service_price(service, currency_symbol=u'£'):
    """Format a price string from a service dictionary

    :param service: a service dictionary, returned from data API

    :return: a formatted price string if the required
             fields are set in the service dictionary.
    """
    if not service.get('priceMin'):
        return ''
    return format_price(
        currency_symbol,
        service.get('priceMin'),
        service.get('priceMax'),
        service.get('priceUnit'),
        service.get('priceInterval'))
