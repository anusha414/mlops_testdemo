inside pod:- curl -X POST http://192.168.0.48:6000/predict -H "Content-Type: application/json" -d '{"text":"I want to cancel my subscription"}'
 
via service:- curl -X POST http://ser1:8080/predict -H "Content-Type: application/json" -d '{"text":"I want to cancel my subscription"}'

curl -X POST --resolve mlops.com:80:10.111.217.186 http://mlops.com/predict -H "Content-Type: 
application/json" -d '{"text":"I want to cancel my subscription"}'
