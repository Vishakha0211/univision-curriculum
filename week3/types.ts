// week 3 - converting the detection data to typescript
// in javascript nothing stops you from putting the wrong type in a field
// typescript catches that before the code even runs

// I started by just writing out what a detection looks like as a type

type Box = {
    x: number
    y: number
    width: number
    height: number
}

type Detection = {
    label: string
    confidence: number
    box: Box
    timestamp: string
}

// a pipeline stage also has a shape
// it can be in one of three states

type StageStatus = "waiting" | "running" | "done"

type PipelineStage = {
    id: string
    name: string
    status: StageStatus
}

// a full pipeline event that the dashboard would receive

type PipelineEvent = {
    event_id: string
    camera_id: string
    timestamp: string
    stage: PipelineStage
    detections: Detection[]
}

// what I noticed when writing this
// the | operator lets you say "this field can only be one of these values"
// that means StageStatus can never be "broken" or "maybe" or undefined
// javascript would allow that and you would find out at runtime
// typescript stops it before the file even runs

// example usage with type checking
const detection: Detection = {
    label: "person",
    confidence: 0.91,
    box: { x: 10, y: 20, width: 50, height: 100 },
    timestamp: "2024-01-15T10:30:00Z"
}

const stage: PipelineStage = {
    id: "stage_1",
    name: "Object detection",
    status: "running"
}

console.log(detection.label)
console.log(stage.status)