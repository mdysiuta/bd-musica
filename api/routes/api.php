<?php

use App\Http\Controllers\ArtistController;
use App\Http\Controllers\LabelController;
use App\Http\Controllers\ReleaseController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::apiResource('releases', ReleaseController::class);
Route::apiResource('artists', ArtistController::class);
Route::apiResource('labels', LabelController::class);