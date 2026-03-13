import './App.css'
import ReleaseList from './components/ReleaseList'
import { releases } from './data'

function App() {
    return (
        <>
            <h1 className='title'>Base de datos de música</h1>
            <hr className='header-separator'/>
            <h2 className='subtitle'>Lista de lanzamientos</h2>
            <ReleaseList releases={releases} />
        </>
    )
}

export default App
