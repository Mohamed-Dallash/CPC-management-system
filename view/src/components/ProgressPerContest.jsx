function ProgressPerContest(props) {
  return (
    <div className="flex flex-col sm:flex-row sm:items-center justify-between w-full border-2 rounded p-4">
      <div className="flex flex-col">
        <a
          target="_blank"
          href={`https://vjudge.net/contest/${props.progressItem?.contest_id}`}
          className="underline text-blue-600"
        >
          {props.progressItem?.topic}
        </a>
        <p>week number : {props.progressItem?.week_number}</p>
      </div>
      <div className="flex flex-col sm:w-60">
        <p>
          {console.log(props.progressItem)}
          solved problems: {props.progressItem?.solved_problems} out of{" "}
          {props.progressItem?.total_problems}
        </p>
        <p>
          zone:{" "}
          {props.progressItem?.zone === "Red" ? (
            <span className="text-red-600">{props.progressItem?.zone}</span>
          ) : props.progressItem?.zone === "Green" ? (
            <span className="text-green-600">{props.progressItem?.zone}</span>
          ) : props.progressItem?.zone === "Yellow" ? (
            <span className="text-yellow-600">{props.progressItem?.zone}</span>
          ) : (
            <span className="text-blue-600">{props.progressItem?.zone}</span>
          )}
        </p>
      </div>
    </div>
  );
}

export default ProgressPerContest;
