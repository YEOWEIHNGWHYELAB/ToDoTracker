// rfc tab for boilerplate
import React, { useEffect, useState } from 'react';
import { Button, Box, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle, DialogActions } from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import { Link } from "react-router-dom";
import useRequestResource from 'src/hooks/useRequestResource';
import ColorBox from "src/components/ColorBox";

export default function Categories() {
    const { getResourceList, resourceList, deleteResource } = useRequestResource({ endpoint: "categories", resourceLabel: "Category" });
    const [open, setOpen] = useState(false);
    const [idToDelete, setIdToDelete] = useState(null);

    useEffect(() => {
        getResourceList();
    }, [getResourceList]) 

    const handleConfirmDelete = (id) => {
        setIdToDelete(id);
        setOpen(true);
    }

    const handleDeleteClose = () => {
        setOpen(false);
    }

    const handleDelete = () => {
        setOpen(false);
        deleteResource(idToDelete);
    }
 
  return (
    <div>
        <Dialog open={open} onClose = {handleDeleteClose}>
            <DialogTitle>
                Are you sure you want to delete this??
            </DialogTitle>
            <DialogActions>
                <Button onClick = {handleDelete}>
                    YES, there is no turning back!
                </Button>
                <Button onClick = {handleDeleteClose}>
                    NO, I want my Mommy
                </Button>
            </DialogActions>
        </Dialog>

        <Box sx={{
            display: "flex",
            justifyContent: "flex-end",
            mb: 4 // Margin bottom
        }}>
            <Button component = {Link} variant = "contained" color = "primary" to="/categories/create">
                Create Category
            </Button>

        </Box>
        Categories List
        <TableContainer component = {Paper}>
            <Table sx={{ minWidth: 360 }} size = "small">
                <TableHead>
                    <TableRow>
                        <TableCell algin = "left">
                            Name
                        </TableCell>

                        <TableCell algin = "left">
                            Color
                        </TableCell>

                        <TableCell algin = "right">
                            Actions
                        </TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {
                        resourceList.results.map((r) => {
                            return <TableRow key={r.id}>
                                <TableCell Align="left">
                                    {r.name}
                                </TableCell>
                                <TableCell Align="left">
                                    <ColorBox color = { `#${r.color}`} />
                                </TableCell>
                                <TableCell Align="right">
                                    <Box sx = {{ display: "flex", justifyContent: "flex-end" }}>
                                        <Link to = {`/categories/edit/${r.id}`} key = "category-edit">
                                            <IconButton size="large">
                                                <EditIcon />
                                            </IconButton>
                                        </Link>
                                        <IconButton size="large" onClick = {() => {
                                            handleConfirmDelete(r.id)
                                        }}>
                                                <DeleteIcon />
                                        </IconButton>
                                    </Box>
                                </TableCell>
                            </TableRow>
                        })
                    }
                </TableBody>
            </Table>
        </TableContainer>
    </div>
  )
}
