import "../style/User.css";

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
function User() {
  return (
    <div>
      <div className="table">
        {calnder.map((days) => (
          <div key={days.id} className="day">
            <h1>{days.day}</h1>
            <div>
              {days.shifts.map((shift, index) => (
                <div key={index} className="shift">
                  <h2>{shift}</h2>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default User;
