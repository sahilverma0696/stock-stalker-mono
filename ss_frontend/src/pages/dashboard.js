import { getData } from "../utils/utils"
import { useEffect,useState } from "react"
import  {CandleStickChart} from "../components/chart"
import { fitWidth } from "react-stockcharts/lib/helper";
import Navbar from "../components/navbar";

export const  Dashboard =()=>{
    let [data, setData] = useState([])

    const fetchGraphData=async()=>{
        let d= await getData();
        setData(d)
        console.log(d)
    }
    useEffect(() => {
        fetchGraphData()
    }, [])
    return (
        <>
        <div><Navbar/></div>
        <div className="px-[80px] grid grid-cols-[250px,auto] gap-10">
            <div>Tab area</div>
            <div id="graph-area" >{data.length!==0?<CandleStickChart type ="hybrid" width={document.getElementById('graph-area').offsetWidth} ratio = {1} data={data}/>:"Graph Area"}</div>
        </div>
        
        </>
    )
} 
