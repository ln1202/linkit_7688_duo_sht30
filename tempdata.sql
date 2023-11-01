SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+08:00";

CREATE TABLE `tempdata` (
  `id` int(100) NOT NULL,
  `temperature` float NOT NULL,
  `humidity` float NOT NULL,
  `device` varchar(10) NOT NULL,
  `intime` varchar(40) NOT NULL,
  `systime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `tempdata`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tempdata`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;
COMMIT;
