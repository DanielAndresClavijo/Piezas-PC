--
-- Base de datos: `piezas_pc_inventario`
--
CREATE DATABASE piezas_pc_inventario;

-- --------------------------------------------------------

USE piezas_pc_inventario;

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id_inventario` int(11) NOT NULL,
  `codigo_barras` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `especificaciones` text COLLATE utf8_spanish_ci NOT NULL,
  `marca` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `precio` int(11) NOT NULL,
  `fecha_inventario` date NOT NULL,
  `id_proveedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id_inventario`, `codigo_barras`, `nombre`, `especificaciones`, `marca`, `precio`, `fecha_inventario`, `id_proveedor`) VALUES
(1, 1234234545, 'RYZEN 5000', 'CPU', 'AMB', 300000, '2020-11-19', 1),
(2, 1234567890, 'Ryzen 5 3400g', 'CPU', 'AMD', 500000, '2020-11-18', 2),
(3, 1234567888, 'Ryzen 7 1700', 'CPU', 'AMD', 320000, '2020-11-18', 1),
(4, 2147483647, 'Samsumg 869 EVO', 'SSD\r\n500gb', 'Samsumg', 200000, '2020-11-19', 2),
(6, 2147483647, 'SSD Chino', 'SSD 480gb', 'chinoSsd', 100000, '2020-11-19', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id_inventario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id_inventario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

