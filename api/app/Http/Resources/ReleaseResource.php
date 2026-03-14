<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class ReleaseResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        $artists = $this->artists()->orderByPivot('position')->select('name')->get();

        return [
            'id' => $this->id,
            'artists' => $artists,
            'title' => $this->title,
            'year' => $this->year,
            'label' => ($this->label != null) ? $this->label->name : null,
            'created_at' => $this->created_at,
            'updated_at'=> $this->updated_at
        ];
    }
}
