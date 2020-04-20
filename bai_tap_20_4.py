from datetime import datetime
# import pytz

local = datetime.now()
print("local:", local.strftime("%m/%d/%Y, %H:%M:%S")) # Chỉ thời gian hiện tại
                                                      # kí hiệu : %m(month) : Tháng  , %H(Hours) : giờ
                                                      #           %d(day) : ngày     , %M(minute) : phút
                                                      #           %Y(Years) : năm    ,%S(seconds) : giây
                                                      # => như vậy khi run chúng ta được kết quả : 04/20/2020, 13:07:08

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/&d/%Y, %H:%M:%S"))