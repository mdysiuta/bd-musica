import type { Release } from "../types"

export default function ReleaseList( {releases} : {releases : Release[]} ) {
    return (
        <div>
            <ul>
                {releases.map((release) => (
                    <li><Release release={release}></Release></li>
                ))}
            </ul>
        </div>
    )
}

function Release( {release} : {release : Release} ) {
    return (
        <li>{release.artist} - {release.name} (<i>{release.year}, {release.label}</i>)</li>
    )
}