class Timelines:

 timelines = {}


 '''
Timeline 1
 '''
 timeline_1 ="""
import PropType from 'prop-types';
import React from 'react';
const @@PageName@@ = ({ current }) => {
    // eslint-disable-next-line no-nested-ternary
  const className = (step) => (current === step
    ? 'bg-[#98c01d]'
    : step < current
      ? 'bg-gray-300'
      : 'bg-gray-300');

  return (
    <div>
      <h2 className="sr-only">@@HeaderText2@@</h2>
      <div
        className="relative after:inset-x-0 after:h-0.5 after:absolute after:top-1/2 after:-translate-y-1/2 after:block after:rounded-lg after:bg-gray-100">
        <ol
          className="relative z-10 flex justify-between text-sm font-medium text-gray-500">
          <li className="flex items-center p-2 bg-white">
            <span className={`w-6 h-6 text-[10px] font-bold leading-6 text-center  text-white ${className(1)} rounded-full`}>
              @@ListRanking1Span@@
            </span>
            <span className="hidden sm:block sm:ml-2"> @@ListRanking1Text@@ </span>
          </li>
          <li className="flex items-center p-2 bg-white">
            <span className={`w-6 h-6 text-[10px] font-bold leading-6 text-center text-white ${className(2)} rounded-full`}>
              @@ListRanking2Span@@
            </span>

            <span className="hidden sm:block sm:ml-2"> @@ListRanking2Text@@ </span>
          </li>
          <li className="flex items-center p-2 bg-white">
            <span className={`w-6 h-6 text-[10px] font-bold leading-6 text-center text-white ${className(3)} rounded-full`}>
              @@ListRanking3Span@@
            </span>
            <span className="hidden sm:block sm:ml-2"> @@ListRanking3Text@@ </span>
          </li>
        </ol>
      </div>
    </div>
  );
};

@@PageName@@.propTypes = {
  current: PropType.number.isRequired
};

export default @@PageName@@;
 """
 timelines["timeline_1"] = timeline_1


 '''
Timeline 2
 '''
 timeline_2 ="""
import React, { useEffect, useState }  from 'react';
const @@PageName@@ = () => {
    
}
export default @@PageName@@;
 """
 timelines["timeline_2"] = timeline_2