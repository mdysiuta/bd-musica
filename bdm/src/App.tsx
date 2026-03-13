import './App.css'
import ReleaseList from './components/ReleaseList'
import { releases } from './data'

function App() {
    return (
        <>
            <h1>Lista de lanzamientos</h1>
            <ReleaseList releases={releases} />
        </>
    )
}

export default App
