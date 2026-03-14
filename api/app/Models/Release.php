<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Release extends Model
{
    protected $fillable = [
        'title',
        'year',
        'label_id',
    ];

    public function artists() : BelongsToMany
    {
        return $this->belongsToMany(Artist::class, 'release_artists');
    }

    public function label() : BelongsTo
    {
        return $this->BelongsTo(Label::class);
    }
}
