import { useState } from "react";
import "../style/User.css";
function User() {
  const [userPick, setUserPick] = useState({});

  function handelUserPik(day, shift) {
    setUserPick((prevUserPick) => {
      const newUserPick = { ...prevUserPick };

      if (newUserPick[day] && newUserPick[day].includes(shift)) {
        newUserPick[day] = newUserPick[day].filter(
          (selectedShift) => selectedShift !== shift
        );
      } else {
        newUserPick[day] = newUserPick[day]
          ? [...newUserPick[day], shift]
          : [shift];
      }

      return newUserPick;
    });
  }

  const calnder = [
    {
      id: 1,
      day: "Sunday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 2,
      day: "Monday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 3,
      day: "Tuesday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 4,
      day: "Wednesday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 5,
      day: "Thursday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 6,
      day: "Friday",
      shifts: ["morning", "evening", "night"],
    },
    {
      id: 7,
      day: "Saturday",
      shifts: ["morning", "evening", "night"],
    },
  ];

  return (
    <div>
      <h1 className="title">
        Hi user!, please pick your preference for the next week
      </h1>
      <div className="table">
        {calnder.map((days) => (
          <div key={days.id} className="day">
            <h1>{days.day}</h1>
            <div>
              {days.shifts.map((shift, index) => (
                <div
                  key={index}
                  className={`shift ${
                    userPick[days.day] && userPick[days.day].includes(shift)
                      ? "selected"
                      : ""
                  }`}
                  onClick={() => handelUserPik(days.day, shift)}
                >
                  <h2>{shift}</h2>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="submit">
        <button className="submit-button" onClick={() => console.log(userPick)}>
          Submit
        </button>
      </div>
    </div>
  );
}

export default User;
