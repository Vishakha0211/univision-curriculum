// week 3 - react component that renders a list of pipeline events
// I wanted to understand how state and rendering work together
// started with hardcoded data, will connect to real data in week 4

import { useState } from "react"

// hardcoded events to start with
const initialEvents = [
    {
        event_id: "evt_001",
        camera_id: "cam_03",
        timestamp: "2024-01-15T10:30:00Z",
        stage: "Object detection",
        status: "done",
        detections: [
            { label: "person", confidence: 0.91 },
            { label: "bicycle", confidence: 0.72 }
        ]
    },
    {
        event_id: "evt_002",
        camera_id: "cam_03",
        timestamp: "2024-01-15T10:30:05Z",
        stage: "Object detection",
        status: "running",
        detections: []
    },
    {
        event_id: "evt_003",
        camera_id: "cam_01",
        timestamp: "2024-01-15T10:30:10Z",
        stage: "Preprocessing",
        status: "waiting",
        detections: []
    }
]

// a single event card
function EventCard({ event }) {
    return (
        <div style={{
            border: "1px solid #ddd",
            borderRadius: "8px",
            padding: "16px",
            marginBottom: "12px",
            background: "white"
        }}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "8px" }}>
                <span style={{ fontSize: "13px", fontWeight: "500" }}>{event.stage}</span>
                <span style={{
                    fontSize: "12px",
                    padding: "2px 8px",
                    borderRadius: "4px",
                    background: event.status === "done" ? "#d4edda" :
                                event.status === "running" ? "#fff3cd" : "#f0f0f0",
                    color: event.status === "done" ? "#1a5c2a" :
                           event.status === "running" ? "#7a5000" : "#555"
                }}>
                    {event.status}
                </span>
            </div>

            <div style={{ fontSize: "12px", color: "#888", marginBottom: "8px" }}>
                {event.camera_id} · {event.timestamp}
            </div>

            {event.detections.length > 0 && (
                <div>
                    {event.detections.map((d, i) => (
                        <span key={i} style={{
                            fontSize: "12px",
                            marginRight: "8px",
                            color: "#444"
                        }}>
                            {d.label} ({(d.confidence * 100).toFixed(0)}%)
                        </span>
                    ))}
                </div>
            )}
        </div>
    )
}

// the main component
export default function PipelineEvents() {
    const [events, setEvents] = useState(initialEvents)
    const [filter, setFilter] = useState("all")

    // filter events by status
    var visible = events
    if (filter !== "all") {
        visible = events.filter(function(e) {
            return e.status === filter
        })
    }

    // simulate adding a new event
    function addEvent() {
        var newEvent = {
            event_id: "evt_00" + (events.length + 1),
            camera_id: "cam_01",
            timestamp: new Date().toISOString(),
            stage: "Preprocessing",
            status: "waiting",
            detections: []
        }
        setEvents([newEvent, ...events])
    }

    return (
        <div style={{ maxWidth: "600px", margin: "40px auto", padding: "0 20px", fontFamily: "sans-serif" }}>
            <h1 style={{ fontSize: "20px", marginBottom: "4px" }}>Pipeline events</h1>
            <p style={{ fontSize: "13px", color: "#666", marginTop: "0", marginBottom: "20px" }}>
                Week 3 - React component practice
            </p>

            <div style={{ display: "flex", gap: "8px", marginBottom: "20px" }}>
                {["all", "waiting", "running", "done"].map(function(f) {
                    return (
                        <button
                            key={f}
                            onClick={function() { setFilter(f) }}
                            style={{
                                padding: "6px 14px",
                                border: "1px solid #ccc",
                                borderRadius: "6px",
                                cursor: "pointer",
                                fontSize: "13px",
                                background: filter === f ? "#222" : "white",
                                color: filter === f ? "white" : "#444"
                            }}
                        >
                            {f}
                        </button>
                    )
                })}
                <button
                    onClick={addEvent}
                    style={{
                        marginLeft: "auto",
                        padding: "6px 14px",
                        border: "1px solid #ccc",
                        borderRadius: "6px",
                        cursor: "pointer",
                        fontSize: "13px",
                        background: "white",
                        color: "#444"
                    }}
                >
                    + add event
                </button>
            </div>

            {visible.length === 0 && (
                <p style={{ fontSize: "13px", color: "#888" }}>no events match this filter</p>
            )}

            {visible.map(function(event) {
                return <EventCard key={event.event_id} event={event} />
            })}
        </div>
    )
}