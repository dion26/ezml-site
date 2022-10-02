import React, {useState} from 'react'

const width = 500;
const height = 350;
const circleRadius = 30;
const initialMousePosition = {x:width/2, y: height/2};

const MouseFollowing = () => {
    
    const [mousePosition, setMousePosition] = useState(initialMousePosition);
    const handleMouseMove = (event:any) => {
        const { clientX, clientY } = event;
        const xMax = 766
        const xMin = 266
        const yMax = 512
        const yMin = 164
        const normX = (clientX - xMin);
        const normY = (clientY - yMin);

        setMousePosition({x: normX, y: normY});
    };
    
    return (
    <div>
        <svg width={width} height={height} onMouseMove={handleMouseMove}>
            <circle 
            cx={mousePosition.x}
            cy={mousePosition.y}
            r={circleRadius}
            />
        </svg>
    </div>
  )
}

export default MouseFollowing
