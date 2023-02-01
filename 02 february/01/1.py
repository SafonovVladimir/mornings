from datetime import datetime


def coupon_code(
        entered_code: str,
        correct_code: str,
        current_date: str,
        expiration_date: str,
) -> bool:

    return entered_code == correct_code and (datetime.strptime(current_date, "%B %d, %Y").date() <= datetime.strptime(expiration_date, "%B %d, %Y").date())



print(coupon_code(
    entered_code="123",
    correct_code="123",
    current_date="July 9, 2015",
    expiration_date="July 9, 2015"
))
#
# print(coupon_code(
#     entered_code="123",
#     correct_code="123",
#     current_date="July 9, 2015",
#     expiration_date="July 2, 2015"
# ))
# current_date = "July 9, 2015"
# date_object = datetime.strptime(current_date, "%B %d, %Y").date()
# print(date_object)



# bday = 'Oct 2, 1869'
#
# import datetime
#
# # Solution
# td = datetime.datetime.strftime(bday, '%m %d, %Y')
# print(td.days)


# from datetime import datetime
#
# date_string = "21 June, 2018"
#
# print("date_string =", date_string)
# print("type of date_string =", type(date_string))
#
# date_object = datetime.strptime(date_string, "%d %B, %Y")
#
# print("date_object =", date_object)
# print("type of date_object =", type(date_object))
