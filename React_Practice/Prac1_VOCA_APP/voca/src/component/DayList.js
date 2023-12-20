import {Link} from "react-router-dom";
// import { useState, useEffect } from "react";
import useFetch from "../hook/useFetch";

export default function DayList() {
    // const [days, setDays] = useState([]);

    // useEffect(() => {
    //     fetch('http://localhost:3001/days')
    //     .then(res => {return res.json()})
    //     .then(data => setDays(data))
    // }, [])

    const days = useFetch("http://localhost:3001/days")

    return (
        <>
            <ul className="list_day">
                {days.map(day => (
                    <li key={day.id}>
                        <Link to={`/day/${day.day}`}>Day {day.day}</Link>
                    </li>
                ))}
            </ul>
        </>
    );
}