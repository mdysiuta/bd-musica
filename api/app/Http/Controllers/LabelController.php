<?php

namespace App\Http\Controllers;

use App\Models\Label;
use Illuminate\Http\Request;

class LabelController extends Controller
{
    /**
     * Mostrar un listado del recurso.
     */
    public function index()
    {
        return Label::all()->toResourceCollection();
    }

    /**
     * Almacenar un recurso creado en la base de datos.
     */
    public function store(Request $request)
    {
        try
        {
            Label::create(['name' => $request['name']]);
        }
        catch (\Exception $e)
        {
            return response()->json(['error' => 'Unable to save label to database.'], 500);
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
