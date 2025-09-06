import React from "react";

export default function EmailItem({ email }) {
  return (
    <div className="border p-4 rounded-md shadow-md mb-3 bg-white">
      <h2 className="font-bold">{email.subject}</h2>
      <p className="text-gray-600 text-sm">{email.sender}</p>
      <p className="mt-2">{email.body_text}</p>
      <div className="mt-2 flex justify-between text-sm text-gray-500">
        <span>Sentiment: {email.sentiment}</span>
        <span>Priority: {email.priority}</span>
      </div>
    </div>
  );
}
