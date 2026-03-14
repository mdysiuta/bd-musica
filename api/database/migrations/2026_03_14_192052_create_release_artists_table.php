<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('release_artists', function (Blueprint $table) {
            $table->bigInteger('release_id');
            $table->bigInteger('artist_id');
            $table->integer('position');
            $table->primary(['release_id', 'artist_id']);
            $table->foreign('release_id')->references('id')->on('releases');
            $table->foreign('artist_id')->references('id')->on('artists');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('release_artists');
    }
};
