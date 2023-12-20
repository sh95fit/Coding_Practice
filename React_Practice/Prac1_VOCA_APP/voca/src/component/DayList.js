import {Link} from "react-router-dom";
import { useState, useEffect } from "react";

export default function DayList() {
    const [days, setDays] = useState([]);
    const [count, setCount] = useState(0);

    useEffect(() => {
        fetch('http://localhost:3001/days')
        .then(res => {return res.json()})
        .then(data => setDays(data))
    }, [])

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