run-server:
	docker compose -p workshop up --build

run-server-locally:
	Make -C api_server run
