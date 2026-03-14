<?php

namespace App\Http\Controllers;

use App\Models\Artist;
use Illuminate\Http\Request;

class ArtistController extends Controller
{
    /**
     * Mostrar un listado del recurso.
     */
    public function index()
    {
        return Artist::all()->toResourceCollection();
    }

    /**
     * Almacenar un recurso creado en la base de datos.
     */
    public function store(Request $request)
    {
        try
        {
            Artist::create(['name' => $request['name']]);
        }
        catch (\Exception $e)
        {
            return response()->json(['error' => 'Unable to save artist to database.'], 500);
        }
    }

    /**
     * Actualizar el recurso especificado en la base de datos.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
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
