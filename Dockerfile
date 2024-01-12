FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /opt/hackergame
COPY requirements.txt /opt/hackergame/
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# Bind project inside instead of copying it
# to avoid copying credentials inside container
# COPY ./ /opt/hackergame/

CMD ["/usr/local/bin/uwsgi", "--ini", "conf/uwsgi-apps/zfun.ini"]
