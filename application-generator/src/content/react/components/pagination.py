class Pagination:

 pagination = {}

 default ="""
import React, { useEffect, useState } from 'react';
import PropType from 'prop-types';

const @@PageName@@ = ({ productsPerPage, totalProducts }) => {
    const [pageNumbers, setPageNumbers] = useState([]);

    useEffect(()=>{   
            let createPageNumbers = [];
            for(let i = 1; i <= Math.ceil(totalProducts / productsPerPage); i++){
                console.log(i)
                createPageNumbers[i] = i
            }
        
        console.log(createPageNumbers)
        setPageNumbers(createPageNumbers);
    }, [])
    
    return (
        <>
            <nav className="flex flex-row justify-end mr-4" aria-label="Page navigation example">
                <ul className="inline-flex items-center -space-x-px">
                    <li>
                    <a href="!#" className="block py-2 px-3 ml-0 leading-tight text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                        <span className="sr-only">@@PreviousText@@</span>
                        <svg aria-hidden="true" className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clipRule="evenodd"></path></svg>
                    </a>
                    </li>
                    {pageNumbers.map(number => 
                        <li key={number}>
                            <a href="!#" className="py-2 px-3 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">{number}</a>
                        </li>
                    )}
                    <li>
                        <a href="!#" className="block py-2 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                            <span className="sr-only">@@NextText@@</span>
                            <svg aria-hidden="true" className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd"></path></svg>
                        </a>
                    </li>
                </ul>
            </nav>
        </>
    )
}

@@PageName@@.propTypes = {
    productsPerPage: PropType.number.isRequired,
    totalProducts: PropType.number.isRequired
}

export default @@PageName@@;
 """
 pagination["default"] = default

 '''
 

 '''
 pagination_1 ="""
const @@PageName@@ = () => {
  
}
export default @@PageName@@;
 """
 pagination["pagination_1"] = pagination_1
 