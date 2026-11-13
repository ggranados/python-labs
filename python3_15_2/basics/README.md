# Basics

Módulos ejecutables con `uv run`.

## Ejecutar comandos

- `uv run app`
- `uv run proctor`
- `uv run greeter`
- `uv run word-counter`
- `uv run temp-converter`

## Ejecutar paquetes o módulos

- `uv run python -m app`
- `uv run python -m proctor`
- `uv run python -m greetings`
- `uv run python -m greetings.greeter`
- `uv run python -m exercises.word_counter`
- `uv run python -m exercises.temp_converter`

## Estructura

- `app/`: punto de entrada principal
- `greetings/`: módulo de saludos
- `exercises/`: ejercicios ejecutables
- `proctor/`: módulo independiente
