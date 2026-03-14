<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Artist extends Model
{
    protected $fillable = [
        'name',
    ];

    public function releases() : BelongsToMany
    {
        return $this->belongsToMany(Release::class, 'release_artists');
    }
}
