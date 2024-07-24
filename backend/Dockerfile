FROM python:3.10

WORKDIR /app
ADD . /app

ARG requirements=requirements/reqs.txt

RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -r $requirements

CMD sh start.sh
