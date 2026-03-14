<?php

namespace App\Http\Controllers;

use App\Models\Release;
use Illuminate\Http\Request;

class ReleaseController extends Controller
{
    /**
     * Mostrar un listado del recurso.
     */
    public function index()
    {
        return Release::all()->toResourceCollection();
    }

    /**
     * Almacenar un recurso creado en la base de datos.
     */
    public function store(Request $request)
    {
        $errorMessage = 'Unable to save release to database.';

        try
        {
            /* Guardar lanzamiento en la base de datos. */

            if(!$request['artist-ids'])
            {
                $errorMessage = 'At least one artist ID must be specified';
                throw new \Exception($errorMessage);
            }

            $release = Release::create([
                'title' => $request['title'],
                'year' => $request['year'],
                'label_id' => $request['label-id'],
            ]);

            /* Asociar al lanzamiento los artistas correspondientes a las IDs entregadas. */

            $artistPosition = 1;
            foreach($request['artist-ids'] as $artistId)
            {
                $release->artists()->attach($artistId, ['position' => $artistPosition]);
                $artistPosition++;
            }
        }
        catch (\Exception $e)
        {
            return response()->json(['error' => $errorMessage], 500);
        }
    }

    /**
     * Mostrar el recurso especificado.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Actualizar el recurso especificado en la base de datos.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remover el recurso especificado de la base de datos.
     */
    public function destroy(string $id)
    {
        //
    }
}
