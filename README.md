# bd-musica
Base de datos de música construída con React.

## Definición de datos
Datos deben ser definidos en un archivo `data.ts` dentro de la carpeta `src/`. Será necesario importar el tipo `Release` desde `types.ts`.

Ejemplo:

```ts
import type { Release } from "./types"

export const releases : Release[] = [
    {
        artist: 'The Beatles',
        name:   'Abbey Road',
        year:   1969,
        label:  'Apple',
    },
    {
        artist: 'Deftones',
        name:   'White Pony',
        year:   2000,
        label:  'Maverick',
    },
]
```