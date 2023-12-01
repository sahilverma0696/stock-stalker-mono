import { getData } from "../utils/utils"
import { useEffect,useState } from "react"
import  {CandleStickChart} from "../components/chart"
import { fitWidth } from "react-stockcharts/lib/helper";
import Navbar from "../components/navbar";
import CandlestickChart from "./chart_new";

const data = [
    // Your candlestick data goes here
    { date: '2023-01-01', open: 100, high: 120, low: 80, close: 110 },
    { date: '2023-01-02', open: 110, high: 130, low: 90, close: 120 },
    // Add more data as needed
  ];

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
        {/* <div>
        <CandlestickChart data={data} />
        </div> */}

        
        </>
    )
} 
