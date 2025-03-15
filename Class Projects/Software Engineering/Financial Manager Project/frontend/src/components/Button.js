import React from 'react'

export default function Button({text, className, onClick =() => {}, type = "button"}) {
    return (
        <button type={type} className={className} onClick={onClick}>
          {text}
        </button>
      );
}
